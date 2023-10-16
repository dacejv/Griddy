
    document.getElementById("chatMsg").disabled = true;
    document.getElementById("Odeslat").disabled = true;
    let otevreno = true;
    let poprve = true;
    focusMethod = async function getFocus() {
        if (otevreno) {
            document.getElementById("chatMsg").disabled = false;
            document.getElementById("Odeslat").disabled = false;
            document.getElementById("chatMsg").focus();
            otevreno = false;
        } else {
            otevreno = true;
            document.getElementById("chatMsg").disabled = true;
            document.getElementById("Odeslat").disabled = true;
        }
        if(poprve){
          poprve = false;
          let newElement = document.createElement('p');
          newElement.className = "bot";
          var today = new Date();
          var time = today.getHours()
          let DivElement = document.createElement('div');
          console.log(time);
          let zacatek;
          const vety = ["Jsem chatovací robot SPŠE Plzeň. Jak Vám mohu pomoci?", "Jsem SPŠE chatbot. Můžu Vám nějak pomoci?", "Jsem chatovací robot SPŠE Plzeň. Co pro Vás mohu udělat?","Jsem chatbot připravený odpovídat na otázky ohledně SPŠE Plzeň. Co Vás zajímá?",];
          const random = vety[Math.floor(Math.random() * vety.length)];
          if((6<=time)&&(time<10)){
            zacatek = "Dobré ráno.";
          }
          if((10<=time)&&(time<12)){
            zacatek = "Dobré dopoledne.";
          }
          if((12<=time)&&(time<17)){
            zacatek = "Dobré odpoledne.";
          }
          if((17<=time)&&(time<20)){
            zacatek = "Dobrý podvečer.";
          }
          if((20<=time)&&(23>=time)){
            zacatek = "Dobrý večer.";
          }
          if((0<=time)&&(time<6)){
            zacatek = "Dobrou noc.";
          }
          newElement.innerHTML = zacatek+" " +random;
          DivElement.appendChild(newElement);
          await delay(550);
          document.getElementById("chat").appendChild(DivElement);
        }
    }

    const messages = document.getElementById("chat");
    const input = document.getElementById("chatMsg");
    input.addEventListener("keyup", function (event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            document.getElementById("Odeslat").click();
        }
    });



    function scrollToBottom() {
        messages.scrollTop = messages.scrollHeight;
    }


    function onbtnclick() {
        const x = document.getElementById("chatMsg");
        if (x.value != "") {
            const newElement = document.createElement('p');
            newElement.className = "uzivatel";
            newElement.innerHTML = x.value;
            document.getElementById("chat").appendChild(newElement);

            scrollToBottom();

            const Val = {"sender": "test_user", "message": x.value};

            const xhr = new XMLHttpRequest();
            xhr.open("POST", "http://localhost:5005/webhooks/rest/webhook/", true);
            xhr.setRequestHeader("Accept", "application/json");
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.setRequestHeader("Authorization", "key");
            const obj = JSON.stringify(Val);
            let start_time = new Date().getTime();
            xhr.send(obj);
            console.log(obj);

            xhr.onreadystatechange = async function () { //asynchroní funkce (pozastaví jenom tuhle metodu na sekundu)
                if (xhr.readyState == 4) {
                    if (xhr.status == 200) {
                        console.log('Time elapsed:', (new Date().getTime() - start_time) / 1000);
                        console.log(xhr.responseText);
                        const obj = JSON.parse(xhr.responseText);
                        for (const key in obj) {
                            let newElement = document.createElement('p');
                            newElement.className = "bot"; // add class name to newElement
                            let obj2 = obj[key];
                            let DivElement = document.createElement('div');
                            if ("undefined" === typeof (obj2.custom)) {
                              newElement.innerHTML = obj2.text;
                              DivElement.appendChild(newElement);
                              document.getElementById("chat").appendChild(DivElement); // append newElement directly
                            }
                          else{
                              newElement.innerHTML = obj2.custom.text; //načte custom text
                              if(obj2.custom.img != ""){  //když je obrázek uložený
                                let DivImgElement = document.createElement('div');
                                let ImgElement = document.createElement('img');
                                let modal = document.createElement("div");
                                modal.className = "modal";
                                DivImgElement.className = "BotImage"
                                ImgElement.src = obj2.custom.img;
                                ImgElement.addEventListener("click", function(){
                                    window.open(obj2.custom.img);
                                });
                                DivImgElement.appendChild(ImgElement);
                                document.getElementById("chat").appendChild(DivImgElement);
                                  
                              }
                              DivElement.appendChild(newElement);
                              if (obj2.custom.url != ""){  
                                  var UrlElement = document.createElement('a');
                                  UrlElement.innerHTML = obj2.custom.url_text;  
                                  UrlElement.href = obj2.custom.url;
                                  UrlElement.target = "_blank";
                                  UrlElement.className = "chatbot-link";
                                  DivElement.appendChild(UrlElement); 
                              }
                              document.getElementById("chat").appendChild(DivElement);  //vypíše se do chatu zpráva
                          }
                          scrollToBottom();
                          await delay(1000);
                        }
                    }
                }
            }
            document.getElementById('chatMsg').value = '';
        }
    }


  function delay(milliseconds){ //metoda pro čekaní sekundy
    return new Promise(resolve => {
        setTimeout(resolve, milliseconds);
    });
  }


function updateScrollbar() {
  $messages.mCustomScrollbar("update").mCustomScrollbar('scrollTo', 'bottom', {
    scrollInertia: 10,
    timeout: 0
  });
}

function setDate(){
  d = new Date()
  if (m != d.getMinutes()) {
    m = d.getMinutes();
    $('<div class="timestamp">' + d.getHours() + ':' + m + '</div>').appendTo($('.message:last'));
  }
}



