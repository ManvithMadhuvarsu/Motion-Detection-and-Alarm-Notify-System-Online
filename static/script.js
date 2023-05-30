function startTracking() {
	var xhr = new XMLHttpRequest();
	xhr.open('POST', '/start_tracking');
	xhr.onload = function() {
	  if (xhr.status === 200) {
		alert('Tracking started!');
	  } else {
		alert('Failed to start tracking. Please try again.');
	  }
	};
	xhr.send();
  }
  
  function goHome() {
	window.location.href = '/';
  }
  
  function displayAbout() {
	var mainDiv = document.querySelector('.main');
	mainDiv.innerHTML = `
	  <h1>About</h1>
	  <h2><b>Objectives<b></h2>
	  <h3> Our main objective is to provide a home-based security notify system which is easy to access and easy to use. The Motion Detection System is a software-based project that aims to automate the process of detecting motion, capturing screenshots, and recording videos when motion is detected in a given area. The system uses computer vision and machine learning techniques to detect motion, and a camera module to capture visual data. The captured data is then stored in a storage unit, which can be accessed remotely through a web-based interface or a mobile application. The system is designed to be reliable, secure, and scalable, and can be used in various applications, including surveillance, security, and home automation.</h3>
	`;
  }
  
  function displayContact() {
	var mainDiv = document.querySelector('.main');
	mainDiv.innerHTML = `
	  <h1>Contact</h1>
	  <p>If you have any questions or suggestions, please contact us at:</p>
	  <p>Email: stark3kstark@gmail.com</p>
	  <p>Phone: +91-6304322533</p>
	`;
  }
  
  // Attach event listeners
  document.querySelector('#startTrackingBtn').addEventListener('click', startTracking);
  document.querySelector('#goHomeBtn').addEventListener('click', goHome);
  document.querySelector('#displayAboutBtn').addEventListener('click', displayAbout);
  document.querySelector('#displayContactBtn').addEventListener('click', displayContact);
  