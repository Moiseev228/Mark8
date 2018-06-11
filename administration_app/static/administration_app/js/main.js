function open_dialog(id_dialog){
    var dialog = document.getElementById(id_dialog);
    dialog.showModal();    
}

function open_waring_dialog(waring_text){
    var dialog = document.getElementById('waring-dialog');
    document.getElementById('waring-text').innerHTML = waring_text;
    dialog.showModal();    
}

function close_window(id_dialog){
    var dialog = document.getElementById(id_dialog);
    dialog.close();    
}

function add_employee(){
    $.ajax({
        type: "GET",
        url: "../new_employee/",
        data:{
            'login':document.getElementById('login').value,
            'password':document.getElementById('password').value,
            'password_repit':document.getElementById('re-password').value,
            'name':document.getElementById('name_employee').value,
            'lastname':document.getElementById('last_name_employee').value,
            'post':document.getElementById('post').value,
            'specialization':document.getElementById('specialization').value,
            'type_users':document.getElementById('type-users').value,
            'phone':document.getElementById('phone').value,
            'address':document.getElementById('address').value,
            'passport':document.getElementById('passport').value,
        },
        dataType: "html",
        cache: false,
        success: function(data){
            if (data == 'ok'){
                location.reload();
            }
            else if(data == 'repit_login'){
                waring_text = 'Пользователь с таким именем уже существует';
                open_waring_dialog(waring_text);
            }
        }
   });
}

function search(){
    var qwery = 'http://127.0.0.1:8000/administration/staff/search?search_term=';
    qwery+=document.getElementById('search-input-staff').value;
    location.replace(qwery);
}

function after_downloading() {
    document.getElementById('login').onfocus = function(){
        if (this.value == 'Логин') {
            this.value = '';
            this.style.color = 'black';
        }
    }
    document.getElementById('login').onblur = function(){
        if (this.value == '') {
            this.value = 'Логин';
            this.style.color = '#b1afaf';
        }
    }

    document.getElementById('password').onfocus = function(){
        if (this.value == 'Пароль') {
            this.value = '';
            this.style.color = 'black';
        }
    }
    document.getElementById('password').onblur = function(){
        if (this.value == '') {
            this.value = 'Пароль';
            this.style.color = '#b1afaf';
        }
    }

    document.getElementById('re-password').onfocus = function(){
        if (this.value == 'Повторите пароль') {
            this.value = '';
            this.style.color = 'black';
        }
    }
    document.getElementById('re-password').onblur = function(){
        if (this.value == '') {
            this.value = 'Повторите пароль';
            this.style.color = '#b1afaf';
        }
    }

    document.getElementById('name_employee').onfocus = function(){
        if (this.value == 'Имя') {
            this.value = '';
            this.style.color = 'black';
        }
    }
    document.getElementById('name_employee').onblur = function(){
        if (this.value == '') {
            this.value = 'Имя';
            this.style.color = '#b1afaf';
        }
    }

    document.getElementById('last_name_employee').onfocus = function(){
        if (this.value == 'Фамилия') {
            this.value = '';
            this.style.color = 'black';
        }
    }
    document.getElementById('last_name_employee').onblur = function(){
        if (this.value == '') {
            this.value = 'Фамилия';
            this.style.color = '#b1afaf';
        }
    }

    document.getElementById('phone').onfocus = function(){
        if (this.value == 'Телефон') {
            this.value = '';
            this.style.color = 'black';
        }
    }
    document.getElementById('phone').onblur = function(){
        if (this.value == '') {
            this.value = 'Телефон';
            this.style.color = '#b1afaf';
        }
    }

    document.getElementById('address').onfocus = function(){
        if (this.value == 'Адрес') {
            this.value = '';
            this.style.color = 'black';
        }
    }
    document.getElementById('address').onblur = function(){
        if (this.value == '') {
            this.value = 'Адрес';
            this.style.color = '#b1afaf';
        }
    }

    document.getElementById('passport').onfocus = function(){
        if (this.value == 'Серия и номер паспорта') {
            this.value = '';
            this.style.color = 'black';
        }
    }
    document.getElementById('passport').onblur = function(){
        if (this.value == '') {
            this.value = 'Серия и номер паспорта';
            this.style.color = '#b1afaf';
        }
    }


    document.getElementById('post').onfocus = function(){
        this.style.color = 'black';
    }
    document.getElementById('post').onblur = function(){
        var numOption = document.getElementById("post").options.selectedIndex;
        if (numOption == 0) {
            this.style.color = '#b1afaf';
        }
    }

    document.getElementById('specialization').onfocus = function(){
        this.style.color = 'black';
    }
    document.getElementById('specialization').onblur = function(){
        var numOption = document.getElementById("specialization").options.selectedIndex;
        if (numOption == 0) {
            this.style.color = '#b1afaf';
        }
    }

    document.getElementById('type-users').onfocus = function(){
        this.style.color = 'black';
    }
    document.getElementById('type-users').onblur = function(){
        var numOption = document.getElementById("type-users").options.selectedIndex;
        if (numOption == 0) {
            this.style.color = '#b1afaf';
        }
    }

    document.getElementById('search-input').onfocus = function(){
        if (this.value == 'Поиск') {
            this.value = '';
            this.style.color = 'black';
        }
    }
    document.getElementById('search-input').onblur = function(){
        if (this.value == '') {
            this.value = 'Поиск';
            this.style.color = '#b1afaf';
        }
    }

    
}