var updateBtns = document.getElementsByClassName('update-cart');
var i=0;
console.log('yahoo');
function myFunction(){
    for(i=0; i< updateBtns.length; i++){
        updateBtns[i].addEventListener('click', function(){
            var prod_id = this.dataset.thing
            var action = this.dataset.action
            console.log('Product ID : ',prod_id, ' Action : ',action);

            // user variable is declared in the 'main' html file so it can be accessed on all pages
            console.log('User: ',user)
            if(user=='AnonymousUser'){
                console.log('User is not authenticated');
            }
            else{
                updateUserOrder(prod_id, action)
            }
        })
    }
}

function updateUserOrder(prod_id, action){
    console.log('User is authenticated, sending data..')
    var url = '/update_item/'

    fetch('http://localhost:3002', {
        method : 'POST',
        headers : {'Content-Type': 'application/json', 'X-CSRF-TOKEN': csrftoken,},
        body : JSON.stringify({'Product ID': prod_id, 'Action': action}),
    })
    .then((Response) => {
        return Response.json()
    })
    .then((data) => {
        location.reload()
    });
}