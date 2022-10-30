import "../css/OrderModal.css";

import closeIcon from "../assets/close-icon.svg";

let xhr = new XMLHttpRequest();

let equalPrice;

function countFinalPrice() {
    var countInfo = document.getElementById("count-info");
    var route = document.getElementById("route").value;
    var timeTo = document.getElementById("time-to").value;
    var count = document.getElementById("num").value;
    // ! fix equal price
    // var equalPrice;

    xhr.open("GET", "http://localhost:8000/tickets_types/get_all_ticket_types");
    xhr.send();
    xhr.onload = function () {
        var tickets_types = JSON.parse(xhr.response);
        equalPrice = count * tickets_types[0].price;
        console.log(equalPrice);
        countInfo.textContent = `\
            Вы выбрали ${count} билетов по маршруту ${route} стоимостью ${equalPrice} р.\
            Это путешествие займет у вас 40 минут. \
            Теплоход отправляется в ${timeTo}.\
        `;
    };
    var timeFromBlock = document.getElementById("time-from-block");
    var timeFrom = document.getElementById("time-from").value;
    if (timeFromBlock.style.display === "flex")
        countInfo.textContent += ` А прибудет в ${timeFrom}.`;
}

function showFromTime() {
    var timeFromBlock = document.getElementById("time-from-block");
    var route = document.getElementById("route").value;
    if (route === "из A в B и обратно в А")
        timeFromBlock.style.display = "flex";
    else timeFromBlock.style.display = "none";
    console.log(timeFromBlock.style.display);
}

function closeModal() {
    var modalWin = document.getElementById("order-modal");
    modalWin.style.display = "none";
}

function OrderModal() {
    return (
        <div id="order-modal" className="order-modal">
            <div>
                <img
                    id="close"
                    className="close-btn"
                    src={closeIcon}
                    onClick={closeModal}
                />
            </div>
            <div className="count-block">
                <div className="order-param">
                    <div className="param-label">Выберите направление:</div>
                    <select
                        id="route"
                        className="param-input"
                        name="route"
                        placeholder="Выберите направление"
                        onChange={showFromTime}
                    >
                        <option value="из A в B">из A в B</option>
                        <option value="из B в A">из B в A</option>
                        <option value="из A в B и обратно в А">
                            из A в B и обратно в А
                        </option>
                    </select>
                </div>

                <div className="order-param">
                    <div className="param-label">
                        Выберите время отправления:
                    </div>
                    <select
                        id="time-to"
                        className="param-input"
                        name="time"
                        placeholder="Выберите время"
                    >
                        <option value="18:00">18:00</option>
                        <option value="18:30">18:30</option>
                        <option value="18:45">18:45</option>
                        <option value="19:00">19:00</option>
                        <option value="19:15">19:15</option>
                        <option value="21:00">21:00</option>
                    </select>
                </div>

                <div id="time-from-block" className="order-param">
                    <div className="param-label">
                        Выберите время возвращения:
                    </div>
                    <select
                        id="time-from"
                        className="param-input"
                        name="time"
                        placeholder="Выберите время"
                    >
                        <option value="18:00">18:00</option>
                        <option value="18:30">18:30</option>
                        <option value="18:45">18:45</option>
                        <option value="19:00">19:00</option>
                        <option value="19:15">19:15</option>
                        <option value="21:00">21:00</option>
                    </select>
                </div>

                <div className="order-param">
                    <div className="param-label">Количество билетов:</div>
                    <input
                        id="num"
                        className="param-input"
                        name="num"
                        defaultValue={1}
                        placeholder="Количество билетов"
                    />
                </div>

                <div className="count-price" onClick={countFinalPrice}>
                    <button>Посчитать</button>
                </div>
            </div>

            <div id="count-info" className="count-info">
                Укажите параметры и нажмите кнопку "посчитать"
            </div>
        </div>
    );
}

export default OrderModal;
