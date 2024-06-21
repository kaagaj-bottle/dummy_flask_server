function getReqCount() {
  fetch('http://127.0.0.1:5000/')
    .then(response => response.json())
    .then(data => {
      console.log(data)
      document.getElementById('reqCount').innerText = `No of responses received: ${data.request_count}`;
    })
    .catch(error => {
      console.error('Error:', error);
    });
}
