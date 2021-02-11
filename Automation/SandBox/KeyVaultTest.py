from azure.keyvault import KeyVaultClient
from azure.common.credentials import ServicePrincipalCredentials

#==========VARIABLES TO BE STORED IN CONFIG==============
SvcPrincipalSecret = "h4TA1jb7/*CSAMwncXbxFrv*0T*HxD0H"
VaultURL = "https://kv-kim-automation.vault.azure.net/" # OK
SecretVersion = "8438cac3f6ca4b228f825c74d724ac80"
#========================================================

#==========VARIABLES TO BE STORED IN CODE================
Tenant = "1e355c04-e0a4-42ed-8e2d-7351591f0ef1" # OK
ClientID = "5378bfcb-197f-4ad1-9f85-054a469af94c"
SecretID = "TEST-SECRET"
#========================================================

#=====Retrieve Atlas Credentials From Key Vault==========
credentials = ServicePrincipalCredentials(client_id=ClientID, secret=SvcPrincipalSecret, tenant=Tenant)
client = KeyVaultClient(credentials)
secret_bundle = client.get_secret(VaultURL, SecretID, SecretVersion)
secret = secret_bundle.value
#========================================================

print(secret)
