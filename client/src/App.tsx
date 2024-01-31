function App() {
    return (
        <>
            <div className="container">
                <form action="">
                    <div className="input-center">
                        <div className="progress">
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

                        <div className="progress">
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
                    </div>

                    <div className="panel"></div>

                    <div className="send">
                        <button>Compute</button>
                    </div>
                </form>
            </div>
        </>
    );
}

export default App;
