import ctypes                               # To load the computer language.
import locale                               # To load the computer language.
import os
import shutil
import win32api                             # Read the Windows login.
import win32net                             # Read the Windows login.

import modules.classes as classes
import modules.automationAux as Aux
import modules.azureConnection as Azure

instance = 'kantarware.visualstudio.com/'


def main():
    try:
        # Read any language to load the directories and paths.
        Aux.loadConfigs('pt')

        # Load the Windows DLL's to inform the computer language.
        windll = ctypes.windll.kernel32
        windll.GetUserDefaultUILanguage()

        # Load the correct file according the language.
        language = locale.windows_locale[windll.GetUserDefaultUILanguage()]
        ### language = 'es_ES' ### For test.
        ### language = 'en_US' ### For test.
        ###language = 'pt_BR' ### For test.

        # Clear the screen.
        os.system('cls')

        # Configure de languages.
        print(f"{classes.Textcolor.GREEN}{Aux.otherConfigs['Translating']}{classes.Textcolor.END}\n")
        if language == 'pt_BR':
            Aux.loadConfigs('pt')  # Change to the Portuguese language.
            print(f"{classes.Textcolor.GREEN}{Aux.otherConfigs['NoTranslating']}{classes.Textcolor.END}\n")
        elif language == 'en_US':
            need_translation, new_hash = Aux.configureLanguage(language='en')
            if need_translation:
                Aux.translateMsg(language='en', new_hash=new_hash)         # Translation.
            else:
                print(f"{classes.Textcolor.GREEN}{Aux.otherConfigs['NoTranslating']}{classes.Textcolor.END}\n")
            Aux.loadConfigs('en')                       # Change to the English language.
        else:  # es_ES
            need_translation, new_hash = Aux.configureLanguage(language='es')
            if need_translation:
                Aux.translateMsg(language='es', new_hash=new_hash)         # Translation.
            else:
                print(f"{classes.Textcolor.GREEN}{Aux.otherConfigs['NoTranslating']}{classes.Textcolor.END}\n")
            Aux.loadConfigs('es')                       # Change to the Spanish language.

        # language
        Aux.otherConfigs['Language'] = language

        # Create the log directory.
        Aux.createDirectory(Aux.directories['LogFolder'])

        # Request the token.
        Aux.accessAzure()

        # Clear the screen.
        os.system('cls')
        # Projects list.
        project = Azure.getProjects()

        test_run_id = input(Aux.otherConfigs['AskRunID']['Msg'])

        # Clear the screen.
        os.system('cls')

        # Start the automation.
        startAutomation(project=project, test_run_id=test_run_id.strip())

    except Exception as ex:
        print(f"{classes.Textcolor.FAIL}{Aux.logs['ErrorMain']['Msg']}{classes.Textcolor.END}", ex)
        Aux.addLogs(Aux.logs["ErrorMain"], str(ex))
        exit(1)


# ======================================================================================================================
# Execute the test case iterations.
def startAutomation(**kwargs):

    # kwargs arguments.
    project = kwargs.get('project')
    test_run_id = kwargs.get('test_run_id')

    try:
        # Complete name (if is using the VPN).
        full_name = win32net.NetUserGetInfo(win32net.NetGetAnyDCName(), win32api.GetUserName(), 2)["full_name"]
    except:
        # Windows login (if is not using the VPN).
        full_name = os.getlogin()

    try:
        testsetpathmanual = Aux.directories["EvidenceFolderManual"]
        Aux.createDirectory(testsetpathmanual)

        # Execute the action to get the manual evidences.
        test_case_id_list, n_iterations_list, id_azure_list, n_test_case_list = Azure.manualEvidences(project,
                                                                                                      test_run_id)

        for test_case_id in test_case_id_list:
            list_steps, name_testcase, summary, cont_steps, change_download_config = Azure.startSteps(project,
                                                                                                      test_case_id)
            step_initial = 0
            step_final = cont_steps
            n_print = 0
            n_iterations = n_iterations_list.pop(0)  # Get the number of the iterations for the test order.
            id_azure = id_azure_list.pop(0)
            n_test_case = n_test_case_list.pop(0)

            # Create the TestSet folder.
            testsetpath = os.path.join(Aux.directories["EvidenceFolder"], Aux.otherConfigs["ETSName"] +
                                       str(test_case_id) + " - " + name_testcase)
            if os.path.exists(testsetpath):
                shutil.rmtree(testsetpath)
            os.makedirs(testsetpath)
            Aux.addLogs("General", Aux.logs["EvidenceFolder"])
            Aux.createDirectory(testsetpath)

            print(f"{classes.Textcolor.WARNING}{Aux.otherConfigs['GeneratingEvidence']['Msg']}"
                  f"{classes.Textcolor.END}\n")
            # Create an EST file.
            word_path = Aux.directories["ESTFile"] + ' ' + Aux.otherConfigs["Language"] + '.docx'

            # Create evidence step by step per Iteration.
            for n_iteration in range(1, n_iterations + 1):
                # Move the prints to the correct folder and rename the evidences - Order by older first.
                filenames = os.listdir(Aux.directories["EvidenceFolderManual"])
                for filename in filenames:
                    if n_print == cont_steps: break
                    if (filename.endswith("png")) and \
                            (("CT" + str(n_test_case) + "-IT" + str(n_iteration)) in filename):

                        file_newname = 'Screenshot_' + str(n_print) + '.png'

                        # Rename the prints and move to the correct Test Case folder.
                        os.rename(os.path.join(testsetpathmanual, filename),
                                  os.path.join(testsetpathmanual, file_newname))
                        shutil.move(os.path.join(testsetpathmanual, file_newname), testsetpath)
                    n_print += 1
                n_print = 0

                est = Aux.wordAddSteps(test_run_id, test_case_id, name_testcase + " - ITERATION " +
                                       str(n_iteration), summary, word_path, testsetpath,
                                       list_steps[step_initial:step_final], "OK", full_name)
                if est is None:
                    Aux.addLogs("General", Aux.logs["ErrorEST"], name_testcase + " - ITERATION " +
                                str(n_iteration))

                pdf = Aux.wordToPDF(est)
                if pdf is None:
                    Aux.addLogs("General", Aux.logs["ErrorConvertPDF"], name_testcase + " - ITERATION " +
                                str(n_iteration))

                if (est is not None) and (pdf is not None):
                    # Add the evidence to the Run and the Test case.
                    Aux.addLogs("General", Aux.logs["ConvertPDF"], name_testcase + " - ITERATION " +
                                str(n_iteration))
                    Azure.SaveEvidenceRun(project, test_run_id, id_azure,
                                          Aux.directories["EvidenceFolder"], Aux.otherConfigs["ETSName"] +
                                          str(test_case_id) + " - " + name_testcase, n_iteration)
                    Azure.SaveEvidenceTestCase(project, Aux.directories["EvidenceFolder"], test_case_id,
                                               Aux.otherConfigs["ETSName"] + str(test_case_id) + " - " +
                                               name_testcase, n_iteration)

                # Clear the evidences prints.
                Aux.deleteFiles(path_log=testsetpath, extension="png")

            n_test_case += 1

        shutil.rmtree(testsetpathmanual)

    except Exception as ex:
        print(f"{classes.Textcolor.FAIL}{Aux.logs['ErrorStartAutomation']['Msg']}{classes.Textcolor.END}", ex)
        Aux.addLogs("General", Aux.logs["ErrorStartAutomation"], str(ex))
        exit(1)

    Aux.addLogs("EndExecution")


# ======================================================================================================================

# ------------------------------------------------------
# Start the automation.
# ------------------------------------------------------
main()
