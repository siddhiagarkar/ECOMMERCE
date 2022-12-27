var updateBtns = document.getElementsByClassName('update-cart');
console.log(updateBtns);
console.log(updateBtns.length);

function myFunction(){
    for(var i=0; i< updateBtns.length; i++){
        console.log("here");
        updateBtns[i].addEventListener('click', function(){
            var prod_id = this.dataset.thing
            var action = this.dataset.action
            console.log('Product ID : ',prod_id, 'Action : ',action);
        })
    }
}
