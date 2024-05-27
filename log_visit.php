<?php
// Define the log file paths
$logFilePath = 'site_visits.log';
$counterFilePath = 'visit_counter.txt';

// Function to increment and get the visit count
function incrementVisitCounter($counterFilePath) {
    if (file_exists($counterFilePath)) {
        $counter = (int)file_get_contents($counterFilePath);
    } else {
        $counter = 0;
    }
    $counter++;
    file_put_contents($counterFilePath, $counter);
    return $counter;
}

// Get the raw POST data
$rawData = file_get_contents("php://input");

// Decode the JSON data
$logData = json_decode($rawData, true);

// Add the visitor's IP address and visit count
$logData['ipAddress'] = $_SERVER['REMOTE_ADDR'];
$logData['visitCount'] = incrementVisitCounter($counterFilePath);

// Append the log data to the file
$logEntry = json_encode($logData) . PHP_EOL;
file_put_contents($logFilePath, $logEntry, FILE_APPEND);

// Respond to the request
header('Content-Type: application/json');
echo json_encode(['status' => 'success', 'visitCount' => $logData['visitCount']]);
?>
