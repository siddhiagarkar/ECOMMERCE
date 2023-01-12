var updateBtns = document.getElementsByClassName('update-cart')
function myf(){
    for(var i=0; i< updateBtns.length; i++){
        updateBtns[i].addEventListener('click', function(){
            var prod_id = this.dataset.thing
            var action = this.dataset.action
            console.log('Product ID : ', prod_id, 'Action : ', action)
        })
    }
}