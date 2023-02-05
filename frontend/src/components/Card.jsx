import "../css/Card.css";

import Time from "./Time";

import durationIconSrc from "../assets/duration-icon.svg";
import infoIcon from "../assets/info-icon.svg";

function showMoreTimes(e) {
    var timesList = e.target.parentElement;
    var times = timesList.querySelectorAll(".time");
    times.forEach((time) => {
        time.hidden = false;
    });
    times[times.length - 1].hidden = true;
}

function showModal() {
    var modalWin = document.getElementById("order-modal");
    modalWin.style.display = "flex";
}

function Card({
    photoSrc,
    title,
    duration,
    price,
    pierPrice,
    tag,
    tagColor,
    tagBgColor,
}) {
    var tagBlock = (
        <div
            className="tag"
            style={{ opacity: 0, color: tagColor, backgroundColor: tagBgColor }}
        >
            {tag}
        </div>
    );
    if (tag)
        tagBlock = (
            <div
                className="tag"
                style={{
                    opacity: 1,
                    color: tagColor,
                    backgroundColor: tagBgColor,
                }}
            >
                {tag}
            </div>
        );

    var pierPriceBlock;
    if (pierPrice)
        pierPriceBlock = (
            <div className="pierPrice">{pierPrice} &#8381; на причале</div>
        );

    return (
        <div className="card">
            <div
                className="card-photo"
                style={{ backgroundImage: "url(" + photoSrc + ")" }}
            >
                {tagBlock}
            </div>

            <div className="card-desc">
                <div className="title">{title}</div>

                <div className="duration">
                    <img className="duration-icon" src={durationIconSrc} />
                    {duration}
                </div>

                <div className="info">
                    <div className="info-item">
                        <img className="info-icon" src={infoIcon} />
                        Билет на целый день
                    </div>

                    <div className="info-item">
                        <img className="info-icon" src={infoIcon} />
                        Неограниченное число катаний
                    </div>

                    <div className="info-item">
                        <img className="info-icon" src={infoIcon} />6 остановок
                        у главных достопримечательностей
                    </div>

                    <div className="info-item">
                        <img className="info-icon" src={infoIcon} />
                        Ближайший рейс сегодня
                    </div>

                    <div className="time-list">
                        <Time time="12:00" />
                        <Time time="13:00" />
                        <Time time="14:00" />
                        <Time time="15:00" />
                        <Time time="16:00" />
                        <Time time="17:00" />
                        <Time time="18:00" />
                        <Time time="19:00" />
                        <Time time="20:00" />
                        <Time time="21:00" />
                        <div
                            className="time"
                            onClick={showMoreTimes}
                            hidden
                        >
                            Ещё...
                        </div>
                    </div>
                </div>

                <div className="details">
                    <div className="prices">
                        <div className="price">{price} &#8381;</div>
                        {pierPriceBlock}
                    </div>

                    <button className="more-info-btn" onClick={showModal}>
                        Подробнее
                    </button>
                </div>
            </div>
        </div>
    );
}

export default Card;
