// import axios from 'axios';

var updateBtns = document.getElementsByClassName('update-cart')
console.log(updateBtns);
function myf(){
    for(var i=0; i< updateBtns.length; i++){
        updateBtns[i].addEventListener('click', function(){
            var prod_id = this.dataset.thing
            var action = this.dataset.action
            console.log('Product ID : ', prod_id, 'Action : ', action);
            updateUserOrder(prod_id, action);
        })
    }
}

function updateUserOrder(prod_id, action){
    console.log(prod_id, action);
    console.log('User is authenticated, sending data...')

    var url = '/update_item/'
    // this url is where you want to send the data

    fetch(url, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body : JSON.stringify({ProductID: prod_id, Action: action}),
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('data : ', data)
    })
}