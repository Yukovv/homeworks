function deleteItem() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            const data = JSON.parse(xhttp.responseText);
            console.log('receive data', data)
            window.location.href = data.url || '/';
        }
    };
    xhttp.open("DELETE", window.location, true)
    xhttp.send();