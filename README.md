# Shell Script Documentation

## Prerequisites:

- Public Repo
- Health Care Repo
- Distribution Repo

#

1.  Keep all the cloned repos or their zipe in the same directoryalong with the `start.sh` file..

```
	Demo-Applications
        ├── distribution-server
        └── distribution-UI
        ├── healthCare-server
        └── healthCare-UI
        ├── public-server
        └── public-UI
        └── start.sh
        └── stop.sh

```

2. Right click and then click on the `New Terminal at Folder` option

   ![image (3)](https://user-images.githubusercontent.com/57682629/147075695-73d4fbf8-c706-4fe9-b1cd-00854d9a477c.png)

3. To be done only ONCE while running the script for the first time. Give execute permission to the shell script.

   ### Run:

   ```
   chmod +x start.sh      ↲
   ```

4. To start ISV-Application

   ### Run:

   ```
    ./start.sh          ↲
   ```

5. User will be prompted for inputs to select an application to start with

   <img width="448" alt="Screenshot 2021-12-22 at 4 12 39 PM (1)" src="https://user-images.githubusercontent.com/57682629/147087734-9547e483-64fb-4b6f-a01f-da5b1a22c4e3.png">

#

## Stop ISV-Application

#

1. Give execute permission to the shell script.

   ### Run:

   ```
   chmod +x stop.sh      ↲
   ```

2. To stop the application servers

   ### Run:

   ```
   ./stop.sh          ↲
   ```
