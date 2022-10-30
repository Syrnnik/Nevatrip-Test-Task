import "../css/Time.css";

function chooseTime(e) {
    var lastChoosen = e.target.parentElement.querySelector("#choosen");
    if (lastChoosen) lastChoosen.id = "";

    if (e.target.id == "choosen") e.target.id = "";
    else e.target.id = "choosen";
}

function Time({ time }) {
    return (
        <div className="time" onClick={chooseTime}>
            {time}
        </div>
    );
}

export default Time;
