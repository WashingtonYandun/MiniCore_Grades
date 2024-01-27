function App() {
    return (
        <div>
            <div>
                <label className="label" htmlFor="dateA">
                    Start Date:
                </label>
                <input type="date" id="dateA" />
                <br />
                <label className="label" htmlFor="dateB">
                    Final Date:
                </label>
                <input type="date" id="dateB" />
            </div>
            <div>
                <button>Compute</button>
            </div>
        </div>
    );
}

export default App;
