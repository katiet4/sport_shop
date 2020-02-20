function validate_form_for_login ( )
{
    var username = document.contact_form.username.value;
    var password = document.contact_form.password.value;
        if (username != "" && password != "")
        {
            if(password.length >= 8){
                     document.contact_form.username.style = 'color:green;';
                     document.contact_form.password.style = 'color:green;';
                     return true;
            }
        }

       document.contact_form.username.style = 'color:red;';
       document.contact_form.password.style = 'color:red;';
       return false
}

function validate_form_for_registration ( )
{
    var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    var email = document.contact_form.email.value;
    var password = document.contact_form.password.value;
    var username = document.contact_form.username.value;
        if ( email != "" && password != "" && username != "")
        {
            if(password.length >= 8){
                if(reg.test(email)){
                     document.contact_form.password.style = 'color:green;';
                     document.contact_form.username.style = 'color:green;';
                     document.contact_form.email.style = 'color:green;';
                     return true;
                }

            }
        }

       document.contact_form.password.style = 'color:red;';
       document.contact_form.username.style = 'color:red;';
       document.contact_form.email.style = 'color:red;';
       return false
}

function validate_for_MSURL ( )
{
    var CkUrl = /^(http|https):\/\/[^ "]+$/;
    var url = document.contact_form.url.value;
        if ( url != "")
        {
                if(CkUrl.test(url)){
                     document.contact_form.url.style = 'color:green;';
                     return true;
                }
        }

       document.contact_form.url.style = 'color:red;';
       return false
}
