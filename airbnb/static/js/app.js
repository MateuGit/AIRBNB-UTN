const pricePerNight = document.getElementById('daily-rate');
const from = document.getElementById('from');
const to = document.getElementById('to');
const summaryPriceNight = document.getElementById('summary-price-night');
const summaryAmountNights = document.getElementById('summary-amount-nights');
const summaryPrice = document.getElementById('summary-price');
const totalPrice = document.getElementById('total-price');
const fee = document.getElementById('fee');
const message = document.getElementById('date-message');
let nights = 1;
let priceNight;
let temporalPrice;
let finalPrice;
let feeNumber;
let dateFrom;
let dateTo;

const events = ()=> {

    from.addEventListener('change', ()=>{

        dateFrom =new Date(from.value);
        console.log(Date.parse(dateFrom)-Date.parse(new Date()))
        if(Date.parse(dateFrom)-Date.parse(new Date()) < 0){

            message.innerHTML = 'no sea imbecil';
            message.style.opacity = 1;
        }else{
            calculateNights();
        }
        
    });
    to.addEventListener('change', ()=>{
        dateTo =new Date(to.value);
        calculateNights();
    });
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
            message.innerHTML = 'no sea imbecil';
            message.style.opacity = 1;
            message.style.margin = '-2rem 0';
        }
    }    
}

const calculate = (value) => {
    
    summaryAmountNights.innerHTML = value == 1 ?  `por 1 noche` : `por ${value} noches`;
    temporalPrice = Number(priceNight) * Number(value);
    summaryPrice.innerHTML ='$' + temporalPrice;
    finalPrice = Number(temporalPrice) + Number(feeNumber);
    totalPrice.innerHTML = '$' + finalPrice;
}

const main = () => {
    summaryPriceNight.innerHTML = pricePerNight.innerHTML;
    priceNight = summaryPriceNight.innerHTML.slice(1);
    calculate(1);
    temporalPrice = Number(priceNight) * Number(nights);
    summaryPrice.innerHTML ='$'+ temporalPrice;
    feeNumber = fee.innerHTML.slice(1);
    finalPrice = Number(temporalPrice) + Number(feeNumber);
    totalPrice.innerHTML = '$' + finalPrice;
    events();
    
}

main();