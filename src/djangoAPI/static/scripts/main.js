var populateHtml = function(data){
    $('#output').addClass('shown');
    $('#from').html('<span class="ttl"> From: </span>' + data.from);
    $('#to').html('<span class="ttl"> To: </span>' + data.to.toString());
    $('#date').html('<span class="ttl"> Date: </span>' + data.date);
    $('#subject').html('<span class="ttl"> Subject: </span>' + data.subject);
}

var openFile = function(event) {
    var input = event.target;
    var reader = new FileReader();
    reader.onload = function(){
        var text = reader.result;
        var node = document.getElementById('output');

        $.ajax({
            type: "POST",
            url: "/email_api/",
            crossDomain: true,
            data:text.toString(),
            success: function (data) {
                populateHtml(data);
            },
            error: function (err) {
                console.log("err");
            }
        });
    };
    reader.readAsText(input.files[0]);
};