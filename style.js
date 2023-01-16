function setFormMessage(formElement, type, message) {
    const messageElement = formElement.querySelector(".form__message");

    messageElement.textContent = message;
    messageElement.classList.remove("form__hidden--success", "form__hidden--error" );
    messageElement.classList.add('form__message--${type}');
}

document.addEventListener("DOMContentLoaded", () => {
    const LoginForm = document.querySelector("#login");
    const createAccountForm = document.querySelector("#createAccount")

    document.querySelector("#linkCreateAccount").addEventListener("click", () => {
        e.preventdefault()
        LoginForm.classList.add("form--hidden");
        createAccountForm.classList.remove("form--hidden");
    });

    document.querySelector("#linkLogin").addEventListener("click", () => {
        e.preventdefault()
        LoginForm.classList.remove("form--hidden");
        createAccountForm.classList.add("form--hidden");
    });

    LoginForm.addEventListener("submit", e => {
        e.preventDefault();

        //perform your AJAX/Fetch login

        setFormMessage(loginForm, "error", "invalid username/password combination");
    })
});
