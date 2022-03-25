:: Warning - calling this batch file will delete the matching
:: targets below from your Azure Storage Account

set target=M98
set aztarget=M98
set imgdate=03152022
:: Below is the location of the Azure Shared Access token for Azure Blob Storage that we must insert for the AzCopy calls to work
set azureblobstoragekey=ENTERSASTOKEN

azcopy rm "https://spaceelements.blob.core.windows.net/sro/%aztarget%/%imgdate%/*%azureblobstoragekey%" --recursive=true