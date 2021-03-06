var api_url='/api/order_list/';

$.getJSON(api_url,function(data){
    console.log(data);
    $('#getcsv').click(function(){
        download('data.csv', get_csv(data));
    });
});

function get_csv(json){
    var fields = Object.keys(json[0]);
    var csv = json.map(function(row){
        return fields.map(function(fieldName){
            return JSON.stringify(row[fieldName] || '');
    });
    });
    csv.unshift(fields);
    return csv.join('\r\n');
}

function download(filename, text) {
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}
