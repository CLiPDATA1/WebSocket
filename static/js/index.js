document.addEventListener('DOMContentLoaded', function(){
    // 문서에서 CSRF 토큰 값을 읽어와서 csrftoken 변수에 할당
    const csrftoken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    document.getElementById('paymentButton').addEventListener('click', function(){
        fetch('/increase_notification/payment/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('paymentCounter').textContent = '지급결재함 카운트: ' + data.카운트;
        })
        .catch(error => {
            console.error(error)
        });
    });
    document.getElementById('collectionButton').addEventListener('click', function(){
        fetch('/increase_notification/collection/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('collectionCounter').textContent = '집금결재함 카운트: ' + data.카운트;
        })
        .catch(error => {
            console.error(error)
        });
    });
    document.getElementById('alarmButton').addEventListener('click', function(){
        fetch('/increase_notification/alarm/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('alarmCounter').textContent = '알람 카운트: ' + data.카운트;
        })
        .catch(error => {
            console.error(error)
        });
    });
});
