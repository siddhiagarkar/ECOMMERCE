console.log('hey hey hey')

var updateBtns = document.getElementsByClassName('update-cart')


for(var i = 0; i < updateBtns.length; i++) {
    
updateBtns[i].addEventListener('click', function() {
    var productId = this.dataset.id
    var action = this.dataset.action
    console.log('clicked - ', productId, ' with action - ', action)

    if(user === 'AnonymousUser'){
        console.log('Not logged in')
    }
    else{
        console.log('User - ' , user)
        updateUserOrder(productId, action)
    }
})
}

function updateUserOrder(productId, action){
    console.log('We made it till here!')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('data: ', data)
        // location.reload()
    })
}