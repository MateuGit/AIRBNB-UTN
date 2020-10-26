const pricePerNight = document.getElementById('daily-rate');
const from = document.getElementById('from');
const to = document.getElementById('to');
const summaryPriceNight = document.getElementById('summary-price-night');
const summaryAmountNights = document.getElementById('summary-amount-nights');
const summaryPrice = document.getElementById('summary-price');
const totalPrice = document.getElementById('total-price');
const fee = document.getElementById('fee');
const message = document.getElementById('date-message');


const MESSAGE_TEXT = 'Ha ingresado una fecha incorrecta';
let nights = 1;
let priceNight;
let temporalPrice;
let finalPrice;
let feeNumber = 0.08;
let feeTotal;
let dateFrom;
let dateTo;

const events = ()=> {

    from.addEventListener('change', ()=>{
        setMinDateToField();
        // dateFrom =new Date(from.value);
        // if(Date.parse(dateFrom)-Date.parse(new Date()) < 0){

        //     message.innerHTML = MESSAGE_TEXT;
        //     message.style.opacity = 1;
        // }else{
        //     calculateNights();
        // }
        
    });
    to.addEventListener('change', ()=>{
        dateTo =new Date(to.value);
        calculateNights();
    });
    
    
}

const calculateLanding = () => {

}

const calculateNights = () => {
    const oneDay = 24 * 60 * 60 * 1000;
    nights = 1;
    if(dateTo){
        const result = Math.round(dateTo - dateFrom) / oneDay;

        if(result > 0){
            calculate(result);
            message.innerHTML = '';
    message.style.margin = '0';
        }else if( result <= 0){
            message.innerHTML = MESSAGE_TEXT;
            message.style.opacity = 1;
            message.style.margin = '-2rem 0';
        }
    }    
}

const calculate = (value) => {
    
    summaryAmountNights.innerHTML = value == 1 ?  `x 1 noche` : `x ${value} noches`;
    temporalPrice = Number(priceNight) * Number(value);
    summaryPrice.innerHTML ='$' + temporalPrice;
    // feeNumber = fee.innerHTML.slice(1);
    feeTotal = Number(temporalPrice) * feeNumber;
    fee.innerHTML = '$' + feeTotal;
    finalPrice = Number(temporalPrice) + Number(feeTotal);
    totalPrice.innerHTML = '$' + finalPrice.toFixed(2);
}

const main = () => {
    summaryPriceNight.innerHTML = pricePerNight.innerHTML;
    priceNight = summaryPriceNight.innerHTML.slice(1);
    calculate(1);
    temporalPrice = Number(priceNight) * Number(nights);
    summaryPrice.innerHTML ='$'+ temporalPrice;
    finalPrice = Number(temporalPrice) + Number(feeTotal);
    console.log(finalPrice)
    console.log(finalPrice)
    console.log(finalPrice)
    console.log(finalPrice)
    console.log(finalPrice)
    console.log(finalPrice)
    console.log(finalPrice)
    console.log(finalPrice)
    totalPrice.innerHTML = '$' + finalPrice.toFixed(2);
    events();
    
}

function setMinDateFromField(){
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
    document.getElementById("from").setAttribute("min", today);
}

function setMinDateToField(){
    if(from.value == ''){
        return;
    }

    let date = from.value.split('-');
    
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

    document.getElementById("to").setAttribute("min", newdate);
}

main();
setMinDateFromField();
setMinDateToField();
