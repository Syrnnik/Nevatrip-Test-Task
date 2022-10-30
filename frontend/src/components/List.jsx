import "../css/List.css";

import Card from "./Card";

import { useEffect } from "react";

import Card1Photo from "../assets/card1.svg";
import Card2Photo from "../assets/card2.svg";
import Card3Photo from "../assets/card3.svg";

function List() {
    useEffect(() => {
        var cards = document.querySelectorAll(".card");
        cards.forEach((card) => {
            var times = card.querySelectorAll(".time");
            if (times.length > 4) {
                for (var i = 4; i < times.length - 1; i++) {
                    times[i].hidden = true;
                }
                times[times.length - 1].hidden = false;
            }
        });
    });

    return (
        <div className="list">
            <Card
                photoSrc={Card1Photo}
                title="Обзорная экскурсия по рекам и каналам 
с остановками Hop on Hop Off 2020"
                duration="2 часа"
                price={900}
                pierPrice={1200}
                tag="Новинка"
                tagColor="#FFF"
            />

            <Card
                photoSrc={Card2Photo}
                title="Обзорная экскурсия по рекам и каналам 
с остановками Hop on Hop Off 2020"
                duration="2 часа"
                price={900}
                pierPrice={1200}
                tag="Круглый год"
                tagColor="#000"
                tagBgColor="#FFD83B"
            />

            <Card
                photoSrc={Card3Photo}
                title="Обзорная экскурсия по рекам и каналам 
с остановками Hop on Hop Off 2020"
                duration="2 часа"
                price={900}
                // pierPrice={1200}
            />
        </div>
    );
}

export default List;
