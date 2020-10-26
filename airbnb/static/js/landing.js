
const paragraphError = document.getElementById('text-error');
const fromLanding = document.getElementById('landing-from');
const toLanding = document.getElementById('landing-to');
const MESSAGE_TEXT = 'Ha ingresado una fecha incorrecta';

const events = () => {
    fromLanding.addEventListener('change', () => {
        setMinDateToField();
        // dateLandingFrom =new Date(fromLanding.value);
        // if(Date.parse(dateLandingFrom)-Date.parse(new Date()) < 0){
    
        //     paragraphError.innerHTML = MESSAGE_TEXT;
        //     paragraphError.style.opacity = 1;
        // }else{
        //     paragraphError.innerHTML = '';
        //     paragraphError.style.opacity = 0;
        // }
    });

    toLanding.addEventListener('change', () => {
        const oneDay = 24 * 60 * 60 * 1000;
        dateLandingTo =new Date(toLanding.value);
        if(dateLandingTo){
            const result = Math.round(dateLandingTo - new Date(fromLanding.value)) / oneDay;
            if(result > 0){
                paragraphError.innerHTML = '';
            }else if( result <= 0){
                paragraphError.innerHTML = MESSAGE_TEXT;
                paragraphError.style.opacity = 1;
            }
        }
    })
}

function setMinDateFrom(){
    let today = new Date();
    let dd = today.getDate();
    let mm = today.getMonth()+1; //January is 0!
    let yyyy = today.getFullYear();
    if(dd<10){
            dd='0'+dd
        } 
        if(mm<10){
            mm='0'+mm
        } 

    today = yyyy+'-'+mm+'-'+dd;
    document.getElementById("landing-from").setAttribute("min", today);
}

function setMinDateToField(){
    if(fromLanding.value == ''){
        return;
    }

    let date = fromLanding.value.split('-');
    
    let dd = date[2]
    let mm = date[1]; //January is 0!
    let yyyy = date[0];
    if(dd<10){
            dd='0'+dd
        } 
        if(mm<10){
            mm='0'+mm
        } 

    let minDate = new Date(yyyy,mm-1,dd);
    minDate.setDate(minDate.getDate() + 1);

    var month = minDate.getUTCMonth() + 1; //months from 1-12
    var day = minDate.getUTCDate();
    var year = minDate.getUTCFullYear();
    
    newdate = year + "-" + month + "-" + day;

    document.getElementById("landing-to").setAttribute("min", newdate);
}


events();
setMinDateFrom();
setMinDateToField();
