Installing Required Tools:
	
	1.For Windows 10, download and install NodeJS and npm from: https://nodejs.org/en/download/
	  During installation process, select the option to install Windows build tools.
	
	2.For Ubuntu/Debian, follow the instruction here to install both NodeJS and npm:
	  https://cloud.google.com/nodejs/docs/setup
	
	3.Follow the instruction in the following link to install Android Studio into your system:
		https://developer.android.com/studio/install
	
	4.Open any project in Android Studio then, 
          open AVD Manager from the button in the top right, where mobile phone icon located then,
	  click on Create Virtual Device button in the bottom left and proceed.

	5.After installation complete, start the virtual device from AVD Manager menu.

Start Frontend:
	
	Open a terminal window in frontend directory and run:
		> npx serve -s build
	Open your internet browser and go to http://localhost:5000

Start Mobile App:
	
	Go to 'mobile' directory then, drag and drop app-release.apk file on to your virtual device. 
	This will install the app into the virtual device, you can start the app from the android app menu.
	Mobile app will ask you your username and password but you can enter any username and password.

	