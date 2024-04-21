let url = `ws://${window.location.host}/chatting/`
        const chatSocket = new WebSocket(url)
        console.log('Chat Socket:', chatSocket)
        chatSocket.onmessage = function(e){
            console.log('Message:', e)
            let data = JSON.parse(e.data)
            console.log('Data:', data)
        }

// document.querySelector('#room-name-input').focus();
//         document.querySelector('#room-name-input').onkeyup = function(e) {
//             if (e.keyCode === 13) {  // enter, return
//                 document.querySelector('#room-name-submit').click();
//             }
//         };

//         document.querySelector('#room-name-submit').onclick = function(e) {
//             var roomName = document.querySelector('#room-name-input').value;
//             window.location.pathname = '/chat/' + roomName + '/';
//         };