class Auth {
     // setup the class and hide the body by default
    constructor() {
        document.querySelector("body").style.display = "none";
        const auth = localStorage.getItem("auth");
        this.validateAuth(auth);
    }
    // check to see if the localStorage item passed to the function is valid and set
    validateAuth(auth) {
        if (auth != 1) {
            window.location.replace("/");
        } else {
            document.querySelector("body").style.display = "block";
        }
    }
    // will remove the localStorage item and redirect to login  screen
    logOut() {
        localStorage.removeItem("auth");
        window.location.replace("/");
    }
}
