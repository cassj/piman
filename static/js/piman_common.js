/* Obviously the auth is actually done on the server and unauth 
 * users won't get any data back but this checks the returned json 
 * for a not_authenticated entry so we can handle it gracefully
 */
function check_authentication( parsed_json ){
  if (parsed_json.not_authenticated){
    return false;
  }
  return true;
}


/* Post a message in the notifications div
 * Will fade onclick or in 5sec
 */
function piman_send_message(msg,error){
 msg = '<span>' + msg + '</span>';

 $(window).scrollTop($('body').position().top)

 $("#notifications_content").html(msg)
   .addClass(error ? 'error' : 'success');
 
 $("#notifications")
   .toggle()
   .delay(5000).fadeOut()
   .click(function(){$(this).stop(true,true).fadeOut()});
 
}

/* Expects the url to return a json construct like {html: ... }
 * the html will be loaded into the #overlay div and it will be 
 * made visible.
 */
function piman_overlay(url){
  var on_success = function(data, textStatus, XMLHttpRequest){
                      try{
                         if(data){
                           if(check_authentication(data)){
                             $("#overlay").html(data.html).show();
                           }else{
                             alert("not logged in");
                           }
                         }
                       }catch(error){
                         $("#header").append("<h1>Error parsing JSON</h1>");
                       }

  }

  var on_error = function(XMLHttpRequest, textStatus, errorThrown){
                    piman_send_message(errorThrown, true);
                    // $("#header").append("<h1 class='error'>Error: " + errorThrown + "</h1>");

                  }
   $.ajax({
    url: url,
    data: {},
  })
  .success(on_success)
  .error(on_error)
}

function piman_clear_overlay(){
  $("#overlay").html('').hide();
}

function piman_fill_show(div, url){
  div = '#' + div;
  var on_success = function(data, textStatus, XMLHttpRequest){
                      try{
                         if(data){
                           if(check_authentication(data)){
                             $(div).html(data.html).show();
                           }else{
                             alert("not logged in");
                           }
                         }
                       }catch(error){
                         $("#header").append("<h1>Error parsing JSON</h1>");
                       }

  }

  var on_error = function(XMLHttpRequest, textStatus, errorThrown){
                    piman_send_message(errorThrown, true);
                    // $("#header").append("<h1 class='error'>Error: " + errorThrown + "</h1>");
                    
                    }

   $.ajax({
    url: url,
    data: {},
  })
  .success(on_success)
  .error(on_error)
}

function piman_clear_hide(div){
  div = '#'+div;
  $(div).html('').hide();
}




var piman_register = function(){
  url = '/accounts/register';
  piman_overlay(url);
}

var piman_edit = function(entity_type, id) {

  url =  '/' + entity_type + '/' + id + '/' + 'edit';
  piman_fill_show('overlay',url);

}

var piman_create = function(entity_type, id){
  url = '/' + entity_type + '/' + 'create';
  piman_overlay(url);
}

var piman_submit = function(formid, url, success, error){

  formid = '#' + formid;
  id = $(formid+" > .id").html();

  if (!success){  
      success = function(data, txt, xhr){piman_send_message("Form successfully submitted " + data.html)};      
  }
  if(!error){
      error = function(xhr, txt, err){piman_send_message("Form submission failed. " + txt, true)};
  }

  $.ajax({type:'POST', 
          url: url,  
          data:$(formid).serialize(), 
          success: success,
          error: error
         });
  
  return(true);
}

