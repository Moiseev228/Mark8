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

function add_recept(){
    $.ajax({
        type: "GET",
        url: "../new_recept/",
        data:{
            'id_prepation':document.getElementById('name_prepations').value,
            'id_patient':document.getElementById('name_patients').value,
            'date_issue':document.getElementById('date_issue').value,
        },
        dataType: "html",
        cache: false,
        success: function(data){
            data = JSON.parse(data);
            if (data['status_responce'] == 'ok'){
                location.reload();
            }
            else if(data=='repit_polis'){
                waring_text = 'Пользователь с таким полисом уже существует';
                open_waring_dialog(waring_text);
            }
        }
   });
}


function after_downloading() {
    document.getElementById('name_patient').onfocus = function(){
        if (this.value == 'Имя пациента') {
            this.value = '';
            this.style.color = 'black';
        }
    }
    document.getElementById('name_patient').onblur = function(){
        if (this.value == '') {
            this.value = 'Имя пациента';
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

    document.getElementById('search-button').onclick = function(){
        // url = window.location.pathname;
        // if (~url.indexOf("staff")) {
        //     location.replace("http://127.0.0.1:8000/administration/staff/");
        // }
        $.ajax({
            type: "GET",
            url: "./search",
            data:{
                'search_term':document.getElementById('search-input').value,
            },
            dataType: "html",
            cache: false,
            success: function(data){
                
            }
       });
       
    }
}