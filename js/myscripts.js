const base_url="http://localhost:3001";

function login() {
    let userName = document.getElementById("username").value;
    let passWord = document.getElementById("password").value;
    let postData =
        '{"username": "' + userName + '", "password": "' + passWord + '" }';
    let url = base_url+"/login";
    let xmlLogin = new XMLHttpRequest();
    xmlLogin.onreadystatechange = function () {
        if (xmlLogin.readyState == 4 && xmlLogin.status == 200) {
            console.log(this.response);
            window.localStorage.setItem('myToken', this.response);
            //lenght of false =5
            if (window.localStorage.getItem('myToken').length == 5) {
                document.getElementById('message').innerHTML = "Wrong username/password";
            }
            else {
                document.getElementById('message').innerHTML = "Login Success";
            }
        }
        else {
            document.getElementById('message').innerHTML = "Something went wrong";
        }
    };
    xmlLogin.open('POST', url, true);
    xmlLogin.setRequestHeader("Content-Type", "application/json");
    xmlLogin.send(postData);
}
  