from collections import Counter
import ctypes                               # To load the computer language.
import locale                               # To load the computer language.
import os
import shutil
import datetime
import win32api                             # Read the Windows login.
import win32net                             # Read the Windows login.
from sys import argv                        # Read command line.


import modules.automationAux as Aux
import modules.automationFunc as Func
import modules.azureConnection as Azure
import modules.classes as classes


def main():
    try:
        # Variables.
        project = None
        id_test_plan = 0
        id_test_suit = 0

        # Read any language to load the directories and paths.
        Aux.loadConfigs('pt')

        # Load the Windows DLL's to inform the computer language.
        windll = ctypes.windll.kernel32
        windll.GetUserDefaultUILanguage()

        # Load the correct file according the language.
        language = locale.windows_locale[windll.GetUserDefaultUILanguage()]
        # language = 'es_CO' ### For test.
        # language = 'en_US'  ### For test.

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

        # Create the export directory.
        Aux.createDirectory(Aux.directories['ExportFolder'])

        # Clear the export folder, if already exist.
        Aux.deleteFiles(path_log=Aux.directories['ExportFolder'], extension='crdownload')

        # Request the token,
        Aux.accessAzure()

        # Clear the screen.
        os.system('cls')

        # Read command line
        if len(argv) != 1:
            project = argv[1]
            id_test_plan = argv[2]
            id_test_suit = argv[3]
            Aux.otherConfigs['ReplaceEvidence'] = argv[4]

        # Ask if want to save the evidences.
        else:
            Aux.askEvidence()

        # Clear the screen.
        os.system('cls')

        # Start the automation.
        project, test_case_id_list, test_run_id = Azure.startRun(project, id_test_plan, id_test_suit)

        startAutomation(project, test_case_id_list, test_run_id)

    except Exception as ex:
        print(f"{classes.Textcolor.FAIL}{Aux.logs['ErrorMain']['Msg']}{classes.Textcolor.END}", ex)
        Aux.addLogs(Aux.logs["ErrorMain"], str(ex))


# ======================================================================================================================
# Execute the test case iterations.
def startAutomation(project: str = None, test_case_id_list: list = None, test_run_id: int = None):
    test_case_id_azure = 100000
    duration = 0
    status = None

    try:
        # Complete name (if is using the VPN).
        full_name = win32net.NetUserGetInfo(win32net.NetGetAnyDCName(), win32api.GetUserName(), 2)["full_name"]
    except:
        # Windows login (if is not using the VPN).
        full_name = os.getlogin()

    try:
        for test_case_id in test_case_id_list:
            list_steps, name_testcase, summary, cont_steps, change_download_config = Azure.startSteps(project,
                                                                                                      test_case_id)
            total_steps = len(list_steps)
            total_iteration = int(total_steps / cont_steps) + 1
            step_initial = 0
            step_final = cont_steps

            # Execution Initial time.
            initial_time = datetime.datetime.now()

            # Validate the testcase name.
            if Aux.validateTestName(name_testcase):
                continue

            # Create the TestSet folder.
            testsetpath = os.path.join(Aux.directories["EvidenceFolder"], Aux.otherConfigs["ETSName"] +
                                       str(test_case_id) + " - " + name_testcase)

            Aux.createDirectory(testsetpath)

            # Ask if need to save the evidence.
            if Aux.otherConfigs['ReplaceEvidence'].upper() in ('S', 'Y'):
                shutil.rmtree(testsetpath)
                os.makedirs(testsetpath)
                Aux.addLogs("General", Aux.logs["EvidenceFolder"])
            else:
                Aux.addLogs("General", Aux.logs["WarningEvidenceFolder"])

            status = "Not Completed"

            # Execute step by step per Iteration.
            for cont_iteration in range(1, total_iteration):

                Aux.addLogs("NewSession", "\nID: " + str(test_case_id) + " - TEST CASE: " +
                            name_testcase + " - ITERATION: " + str(cont_iteration) + "\n")

                print(f"{classes.Textcolor.BOLD}{name_testcase}{classes.Textcolor.END}")
                status, step_failed = executeStepByStep(list_steps, testsetpath, step_initial, step_final,
                                                        change_download_config)

                # If fail / abort in a iteration, jump to the next iteration.
                if status == "Failed":
                    Func.verifyBrowser()
                elif status == "Aborted":
                    Func.verifyBrowser()
                    comments = Aux.otherConfigs['DownloadingFileIE']['Msg']
                else:
                    comments = Azure.getInfoRun(project, test_run_id, test_case_id_azure, name_testcase, cont_iteration,
                                                step_failed, status)

                # Set the test case duration.
                duration = datetime.datetime.now() - initial_time
                duration = int(duration.total_seconds() * 1000)

                # Process to generate the evidences and save to Azure.
                if Aux.otherConfigs["ReplaceEvidence"].upper() in ('S', 'Y'):
                    # Update the test case inside the Run.
                    Azure.updateTestCaseRun(project, test_run_id, test_case_id_azure, status, duration, comments)

                    print(f"{classes.Textcolor.WARNING}{Aux.otherConfigs['GeneratingEvidence']['Msg']}{classes.Textcolor.END}\n")

                # If aborted do not create evidences.
                if Aux.otherConfigs["ReplaceEvidence"].upper() in ('S', 'Y') and status != 'Aborted':
                    # Create an EST file.
                    word_path = Aux.directories["ESTFile"] + ' ' + Aux.otherConfigs["Language"] + '.docx'

                    est = Aux.wordAddSteps(test_run_id, test_case_id, name_testcase + " - ITERATION " +
                                           str(cont_iteration), summary, word_path, testsetpath,
                                           list_steps[step_initial:step_final], step_failed, full_name)
                    pdf = Aux.wordToPDF(est)

                    if est is None:
                        Aux.addLogs("General", Aux.logs["ErrorEST"], name_testcase + " - ITERATION " +
                                    str(cont_iteration))

                    if pdf is None:
                        Aux.addLogs("General", Aux.logs["ErrorConvertPDF"], name_testcase + " - ITERATION " +
                                    str(cont_iteration))

                    if (est is not None) and (pdf is not None):
                        # Add the evidence to the Run and the Test case.
                        Aux.addLogs("General", Aux.logs["ConvertPDF"], name_testcase + " - ITERATION " +
                                    str(cont_iteration))
                        Azure.SaveEvidenceRun(project, test_run_id, test_case_id_azure,
                                              Aux.directories["EvidenceFolder"], Aux.otherConfigs["ETSName"] +
                                              str(test_case_id) + " - " + name_testcase, cont_iteration)
                        Azure.SaveEvidenceTestCase(project, Aux.directories["EvidenceFolder"], test_case_id,
                                                   Aux.otherConfigs["ETSName"] + str(test_case_id) + " - " +
                                                   name_testcase, cont_iteration)

                    # Clear the evidences prints.
                    Aux.deleteFiles(path_log=testsetpath, extension="png")

                # Variables.
                step_initial = step_final
                step_final = step_final + cont_steps

            test_case_id_azure += 1

    except Exception as ex:
        print(f"{classes.Textcolor.FAIL}{Aux.logs['ErrorStartAutomation']['Msg']}{classes.Textcolor.END}", ex)
        Aux.addLogs("General", Aux.logs["ErrorStartAutomation"], str(ex))
        Azure.updateTestCaseRun(project, test_run_id, test_case_id_azure, name_testcase, step_failed, cont_iteration,
                                status, duration)
        Azure.updateRun(project, test_run_id, "Aborted")

    # Update the Run status.
    if Aux.otherConfigs["ReplaceEvidence"].upper() in ('S', 'Y'):
        Azure.updateRun(project, test_run_id, "Completed")
    Aux.addLogs("EndExecution")


# ======================================================================================================================
# Execute the test case steps.
def executeStepByStep(list_steps: list, testsetpath: str = None, step_initial: int = None, step_final: int = None,
                      change_download_config: bool = False):
    element = None
    step_order = 0
    step_failed = None
    status_steps = []

    try:
        for step in list_steps[step_initial:step_final]:
            # Initialize the variables.
            value1 = None
            value2 = None

            verb = step.split()[0]
            # Don't execute the step with 'No' / 'Não'.
            if verb in ('"No"', '"Não"', '"No"'.replace('"', ''), '"Não"'.replace('"', '')):
                verb = 'NoExecute'
                pattern = Aux.regex.compile('(?:"Não"|"No")')
                step = Aux.regex.sub(pattern, '', step).strip()
            else:
                pattern = Aux.regex.compile('(?:"Sim"|"Si"|"Yes")')
                step = Aux.regex.sub(pattern, '', step).strip()
                verb = step.split()[0]

            if step.count('"') >= 3:  # More than one parameter.
                value1 = step.split('"')[1]
                value2 = step.split('"')[3]
            elif step.count('"') == 2:  # One parameter.
                value1 = step.split('"')[1]

            print(f"{Aux.otherConfigs['Step']['Msg']}: {step}")
            print(f"{Aux.otherConfigs['Verb']['Msg']}: {verb}")
            print(f"PARAM 1: {value1}")
            print(f"PARAM 2: {value2}")
            print(f"=+=" * 30)

            # Execute the test step.
            element, status_step = eval(Aux.verbs[verb])(element=element, value1=value1, value2=value2, step=step,
                                                         change_download_config=change_download_config)

            if status_step == "Failed":
                step_failed = step_order
                status_steps.append("Failed")
            elif status_step == "Aborted":
                step_failed = step_order
                status_steps.append("Aborted")
                return "Aborted", step_failed
            else:
                status_steps.append("Passed")

            # Take the screenshot of each step, except to the NoExecute step.
            if Aux.otherConfigs["ReplaceEvidence"].upper() in ('S', 'Y') and verb != 'NoExecute':
            # if Aux.otherConfigs["ReplaceEvidence"].upper() in ('S', 'Y') and verb not in ('NoExecute', 'Fechar', 'Cerrar', 'Close'):
                imagename = Aux.otherConfigs["EvidenceName"] + str(step_order) + Aux.otherConfigs[
                    "EvidenceExtension"]
                if not Aux.takePicture(testsetpath, imagename):
                # if not Func.takePicture(testsetpath, imagename):
                    Aux.addLogs("General", Aux.logs["ErrorScreenshot"], step)

            step_order += 1

        # Set the test case status.
        status_counter = Counter(status_steps)
        if status_counter['Failed'] != 0:
            status_ct = "Failed"
        else:
            status_ct = "Passed"

        return status_ct, step_failed

    except Exception as ex:
        print(f"{classes.Textcolor.FAIL}{Aux.logs['ErrorExecuteStepByStep']['Msg']}{classes.Textcolor.END}", ex)
        Aux.addLogs("General", Aux.logs["ErrorExecuteStepByStep"], str(ex))


# ------------------------------------------------------
# Start the automation.
# ------------------------------------------------------
main()
