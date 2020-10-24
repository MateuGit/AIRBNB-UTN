
const paragraphError = document.getElementById('text-error');
const fromLanding = document.getElementById('landing-from');
const toLanding = document.getElementById('landing-to');
const MESSAGE_TEXT = 'Ha ingresado una fecha incorrecta';

const events = () => {
    fromLanding.addEventListener('change', () => {
        
        dateLandingFrom =new Date(fromLanding.value);
        if(Date.parse(dateLandingFrom)-Date.parse(new Date()) < 0){
    
            paragraphError.innerHTML = MESSAGE_TEXT;
            paragraphError.style.opacity = 1;
        }else{
            paragraphError.innerHTML = '';
            paragraphError.style.opacity = 0;
        }
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

events();