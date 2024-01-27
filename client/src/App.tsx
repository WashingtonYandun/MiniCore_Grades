import { useState, useEffect } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";

function App() {
    return (
        <div>
            <div className="filtros">
                <label className="label" htmlFor="fechaVenta">
                    Fecha de Venta:
                </label>
                <input className="fechas" type="date" id="fechaVenta" />

                <label className="label" htmlFor="fechaFin">
                    Fecha Final:
                </label>
                <input className="fechas" type="date" id="fechaFin" />
            </div>

            <div>
                <button>Buscar</button>
            </div>
        </div>
    );
}

export default App;
