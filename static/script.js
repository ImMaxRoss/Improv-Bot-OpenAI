window.onload = function() {
  // Get the width and height of the window
  var windowWidth = window.innerWidth;
  var windowHeight = window.innerHeight;

  // Create an array to store the stars
  var stars = [];

  // Create a function to generate a random number between a min and max value
  function random(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

  // Create a function to generate the stars
  function createStars() {
	  console.log("createStars() function called");
    // Set the number of stars to generate
    var numStars = 450;

    // Create the stars
    for (var i = 0; i < numStars; i++) {
      var star = document.createElement("div"); // Create a div element for the star
      star.className = "star"; // Set the class of the star to "star"
      star.style.top = random(0, windowHeight) + "px"; // Set the top position of the star
      star.style.left = random(0, windowWidth) + "px"; // Set the left position of the star
      stars.push(star); // Add the star to the array
      document.body.appendChild(star); // Add the star to the page
    }
	
  }

  // Call the createStars function to generate the stars
  createStars();
};
