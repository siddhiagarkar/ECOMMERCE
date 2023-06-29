console.log("spain")

const btn = document.getElementById('button-59')
const username = document.getElementById('username')
const f_name = document.getElementById('f_name')
const l_name = document.getElementById('l_name')
const email = document.getElementById('email')

console.log(username.innerHTML)
btn.addEventListener('click', () => {
    console.log('pressed')

    if(btn.innerHTML == 'EDIT'){
        createNewElement();
        btn.innerText = 'SAVE'
    }
    else{
        btn.innerText = 'EDIT'
    }

})


function createNewElement() {
    var previous_username = document.getElementById('username').innerHTML;
    var previous_f_name = document.getElementById('f_name').innerHTML;
    var previous_l_name = document.getElementById('l_name').innerHTML;
    var previous_email = document.getElementById('email').innerHTML;

    // Create a new input element
    var new_u_input = document.createElement('input');
    new_u_input.setAttribute('type', 'text');
    new_u_input.setAttribute('id', 'new_inputBox');
    new_u_input.setAttribute('value', previous_username);

    var new_f_input = document.createElement('input');
    new_f_input.setAttribute('type', 'text');
    new_f_input.setAttribute('id', 'new_inputBox');
    new_f_input.setAttribute('value', previous_f_name);

    var new_l_input = document.createElement('input');
    new_l_input.setAttribute('type', 'text');
    new_l_input.setAttribute('id', 'new_inputBox');
    new_l_input.setAttribute('value', previous_l_name);

    var new_e_input = document.createElement('input');
    new_e_input.setAttribute('type', 'email');
    new_e_input.setAttribute('id', 'new_inputBox');
    new_e_input.setAttribute('value', previous_email);

    // Replace the username element with the new input element
    document.getElementById('username').innerHTML = new_u_input.outerHTML;
    document.getElementById('f_name').innerHTML = new_f_input.outerHTML;
    document.getElementById('l_name').innerHTML = new_l_input.outerHTML;
    document.getElementById('email').innerHTML = new_e_input.outerHTML;

}