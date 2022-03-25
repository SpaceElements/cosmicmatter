set target=m3
set aztarget=m3
set imgdate=03202022
:: Below is the location of the Azure Shared Access token for Azure Blob Storage that we must insert for the AzCopy calls to work
set azureblobstoragekey=ENTERSASTOKEN

cd\
cd "Users\Space\Desktop\%target%"
md bias
md dark
md lum
md red
md green
md blue
md ha
md o3
md s2
@echo off
echo ...
echo ... [96mThe following sub-directories were created:[0m
echo ... 
echo ... [91mbias, dark, lum, red, green, blue, ha, o3, s2[0m
@echo on

azcopy copy "https://spaceelements.blob.core.windows.net/sro/%aztarget%/%imgdate%/localhashlog/*%azureblobstoragekey%" c:\users\space\Desktop\%target%\rar-output\ 

azcopy copy "https://spaceelements.blob.core.windows.net/sro/%aztarget%/%imgdate%/bias/*%azureblobstoragekey%" c:\users\space\Desktop\%target%\rar-output\ 

azcopy copy "https://spaceelements.blob.core.windows.net/sro/%aztarget%/%imgdate%/lum/*%azureblobstoragekey%" c:\users\space\Desktop\%target%\rar-output\ 

azcopy copy "https://spaceelements.blob.core.windows.net/sro/%aztarget%/%imgdate%/dark/*%azureblobstoragekey%" c:\users\space\Desktop\%target%\rar-output\ 

azcopy copy "https://spaceelements.blob.core.windows.net/sro/%aztarget%/%imgdate%/red/*%azureblobstoragekey%" c:\users\space\Desktop\%target%\rar-output\ 

azcopy copy "https://spaceelements.blob.core.windows.net/sro/%aztarget%/%imgdate%/green/*%azureblobstoragekey%" c:\users\space\Desktop\%target%\rar-output\ 

azcopy copy "https://spaceelements.blob.core.windows.net/sro/%aztarget%/%imgdate%/blue/*%azureblobstoragekey%" c:\users\space\Desktop\%target%\rar-output\ 

azcopy copy "https://spaceelements.blob.core.windows.net/sro/%aztarget%/%imgdate%/ha/*%azureblobstoragekey%" c:\users\space\Desktop\%target%\rar-output\ 

azcopy copy "https://spaceelements.blob.core.windows.net/sro/%aztarget%/%imgdate%/o2/*%azureblobstoragekey%" c:\users\space\Desktop\%target%\rar-output\ 

azcopy copy "https://spaceelements.blob.core.windows.net/sro/%aztarget%/%imgdate%/s3/*%azureblobstoragekey%" c:\users\space\Desktop\%target%\rar-output\ 

@echo off
echo ...
echo ... [96mBeginning Compression:[0m
echo ... 
echo ... [91mUsing %vsize% MB RAR file size limits[0m
@echo on
c:\"program files\winrar\rar.exe" e c:\"users\space\desktop\%target%\rar-output\bias.part01.rar" c:\"users\space\desktop\%target%\bias\"
c:\"program files\winrar\rar.exe" e c:\"users\space\desktop\%target%\rar-output\lum.part01.rar" c:\"users\space\desktop\%target%\lum\"
c:\"program files\winrar\rar.exe" e c:\"users\space\desktop\%target%\rar-output\dark.part01.rar" c:\"users\space\desktop\%target%\dark\"
c:\"program files\winrar\rar.exe" e c:\"users\space\desktop\%target%\rar-output\red.part01.rar" c:\"users\space\desktop\%target%\red\"
c:\"program files\winrar\rar.exe" e c:\"users\space\desktop\%target%\rar-output\green.part01.rar" c:\"users\space\desktop\%target%\green\"
c:\"program files\winrar\rar.exe" e c:\"users\space\desktop\%target%\rar-output\blue.part01.rar" c:\"users\space\desktop\%target%\blue\"
c:\"program files\winrar\rar.exe" e c:\"users\space\desktop\%target%\rar-output\ha.part01.rar" c:\"users\space\desktop\%target%\ha\"
c:\"program files\winrar\rar.exe" e c:\"users\space\desktop\%target%\rar-output\o3.part01.rar" c:\"users\space\desktop\%target%\o3\"
c:\"program files\winrar\rar.exe" e c:\"users\space\desktop\%target%\rar-output\s2.part01.rar" c:\"users\space\desktop\%target%\s2\"

