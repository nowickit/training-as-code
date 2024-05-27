 // Function to get visitor information
 function getVisitorInfo() {
	return {
		url: window.location.href,
		referrer: document.referrer,
		userAgent: navigator.userAgent,
		language: navigator.language,
		screenResolution: `${window.screen.width}x${window.screen.height}`,
		viewportSize: `${window.innerWidth}x${window.innerHeight}`,
		timestamp: new Date().toISOString()
	};
}

// Function to send log data to the server
function logVisit(visitorInfo) {
	fetch('log_visit.php', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(visitorInfo)
	}).catch(error => console.error('Error logging visit:', error));
}

// Gather visitor information and log it
const visitorInfo = getVisitorInfo();
logVisit(visitorInfo);