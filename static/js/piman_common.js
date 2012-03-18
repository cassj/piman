/* piman_edit("entity_type", "id") 
 *  This basically does an Ajax request to grab the CRUD form at /entity_type/id
 *  and shows it in a pop up - unsure how to implement this at the moment. Should
 *  it be an iframe so the back button works? Can you do that and toggle its
 *  visibility so it shows as an overlay without messing up the rest of the page 
 *  format?
 *  
*/

function check_authentication( parsed_json ){
  if (parsed_json.not_authenticated){
    return false;
  }
  return true;
}

function send_notification(message){
  $("notifications").html("<p>" + message + "</p>");
  setTimeout( function(){
                       $('notifications').show('slow').delay(5000).hide('slow');
                        },
              0
  );
}

var piman_edit = function(entity_type, id) {

  url =  '/' + entity_type + '/' + id + '/' + 'edit';

  //alert(url);


  // submit a post request to the url with no data
  // you should get the empty form back, unless you get json
  $.ajax({
    data: { },
    datatype: 'json',
    success: function(data, textStatus, XMLHttpRequest){
               if(data){
                 if(check_authentication(data)){
                   $("#overlay").html(data.html);
                 }else{
                   // this should just redirect the top page to the login page.
                   alert("not logged in");
                 }
               }
             },
    type: 'POST',
    url: url
  });
}


