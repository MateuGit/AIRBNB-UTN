const pricePerNight = document.getElementById('daily-rate');
const from = document.getElementById('from');
const to = document.getElementById('to');
const summaryPriceNight = document.getElementById('summary-price-night');
const summaryAmountNights = document.getElementById('summary-amount-nights');
const summaryPrice = document.getElementById('summary-price');
const totalPrice = document.getElementById('total-price');
const fee = document.getElementById('fee');
const message = document.getElementById('date-message');
const disabledDate = [];
const reserveBtn = document.getElementById('reserve-btn');

const MESSAGE_TEXT = 'Fecha no disponible';
let nights = 1;
let priceNight;
let temporalPrice;
let finalPrice;
let feeNumber = 0.08;
let feeTotal;
let dateFrom;
let dateTo;

const events = () => {

    from.addEventListener('change', () => {
        setMinDateToField();
        const date = new Date(from.value);
        message.style.opacity = 0;
        reserveBtn.disabled = false;
        disabledDate.forEach(element => {
            if ((element.getDate() == date.getDate()) && (element.getDate() == date.getDate())) {
                message.innerHTML = MESSAGE_TEXT;
                message.style.opacity = 1;
                message.style.margin = '-2rem 0';
                reserveBtn.disabled = true;
                return;
            }

        })


    });
    to.addEventListener('change', () => {
        dateTo = new Date(to.value);
        
        calculateNights();
    });


}

const calculateLanding = () => {

}

const calculateNights = () => {
    const oneDay = 24 * 60 * 60 * 1000;
    nights = 1;
    if (dateTo) {
        const result = Math.round(dateTo - new Date(from.value)) / oneDay;
        if (result > 0) {
            message.innerHTML = '';
            message.style.opacity = 0;
            reserveBtn.disabled = false;
            calculate(result); 
        }else{
            message.innerHTML = 'Fecha incorrecta';
            message.style.opacity = 1;
            message.style.margin = '-2rem 0';
            reserveBtn.disabled = true;
        }
    }
}

const calculate = (value) => {

    summaryAmountNights.innerHTML = value == 1 ? `x 1 noche` : `x ${value} noches`;
    temporalPrice = Number(priceNight) * Number(value);
    summaryPrice.innerHTML = '$' + temporalPrice;
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
    summaryPrice.innerHTML = '$' + temporalPrice;
    finalPrice = Number(temporalPrice) + Number(feeTotal);
    totalPrice.innerHTML = '$' + finalPrice.toFixed(2);
    events();

}

function setMinDateFromField() {
    let today = new Date();
    let dd = today.getDate();
    let mm = today.getMonth() + 1; //January is 0!
    let yyyy = today.getFullYear();
    if (dd < 10) {
        dd = '0' + dd
    }
    if (mm < 10) {
        mm = '0' + mm
    }

    today = yyyy + '-' + mm + '-' + dd;
    document.getElementById("from").setAttribute("min", today);
}

function setMinDateToField() {
    if (from.value == '') {
        return;
    }

    let date = from.value.split('-');

    let dd = date[2]
    let mm = date[1]; //January is 0!
    let yyyy = date[0];
    if (dd < 10) {
        dd = '0' + dd
    }
    if (mm < 10) {
        mm = '0' + mm
    }

    let minDate = new Date(yyyy, mm - 1, dd);
    minDate.setDate(minDate.getDate() + 1);

    var month = minDate.getUTCMonth() + 1; //months from 1-12
    var day = minDate.getUTCDate();
    var year = minDate.getUTCFullYear();

    newdate = year + "-" + month + "-" + day;

    document.getElementById("to").setAttribute("min", newdate);
}

const getDisabledDates = () => {
    const ulDates = document.getElementById('disabled-dates');

    ulDates.childNodes.forEach(element => {
        if (element.innerHTML) {
            disabledDate.push(new Date(element.innerHTML));
        }
    });

}

main();
setMinDateFromField();
setMinDateToField();
getDisabledDates();
console.log(disabledDate);