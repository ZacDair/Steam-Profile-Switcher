# Desktop app to facilitate switching profiles
This project is purely an automation tool.
  
## Work in progress project. ##  
  
Currently the goal is to produce a desktop application in python that allows the user to store multiple profiles,.  
Each profile is a name, bio and avatar.  
Do not mistake a profile for an account, although this system is still built to work with multiple accounts, it works on the basis of one logged in at any given time.  
  
These profiles can then be switched easily.
To achieve this functionality a reverse engineered version of Steam's login system was required.  
  
More updates and info soon. 

### Quick Progress List: ###  

- [x] MVC base structure implemented  
- [x] Create profile functionality  
- [x] Delete profile functionality  
- [x] GUI to support our features  
- [x] Revese engineered Steam login  
- [ ] Improve login time (30secs is way too long)  
- [x] Convert login to a background process - ended up being a thread  
- [ ] Use the return result of the login  
- [ ] Potentially implement a login on load feature (requires storing the password locally)  
- [ ] Stay logged in implementation  
- [ ] Help content to be written  
- [ ] Merge old config window functionality
- [ ] Fix profile details image display  
- [ ] Test captcha image display  
- [ ] Log out functionality (Research and implement)  
- [ ] Switch functionality needs to be implemented and triggered by the button  
- [ ] Clean and Optimize (reocurring process)  
- [ ] Convert project to launch properly on main.py run  
- [ ] Add dependecies error checking  
- [ ] Package and create installer  

