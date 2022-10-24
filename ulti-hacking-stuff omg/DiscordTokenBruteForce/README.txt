FOR EDUCATIONAL PURPOSES ONLY!!

NEEDED RESOURCES:
LIBRARIES: strng, base64, os, threading
DiscordUserID

FOR DISCORD TOKEN LOGIN:
https://discord.com/login > CTRL+SHIFT+I > console > copy this code:

function login(token) {
setInterval(() => {
document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
}, 50);
setTimeout(() => {
location.reload();
}, 2500);
}

login('PASTE TOKEN HERE')

 INSTEAD OF PASTE TOKEN HERE < PASTE YOUR GENERATED TOKEN THERE (the ' ' must stay there)

GLHF