import {useState, useEffect} from "react";

function CustomerDisplay() {
    const [record, setRecord] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch("http://127.0.0.1:5000/api/customers/customer_58487570992442be85494912cb4b8a37") // Replace with your API URL
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.json();
            })
            .then((data) => {
                setRecord(data);
                setLoading(false);
            })
            .catch((error) => {
                setError(error.message);
                setLoading(false);
            });
    }, []);

    return (
        <div style={styles.container}>
            <h2>Record Details</h2>
            {loading && <p>Loading...</p>}
            {error && <p style={styles.error}>{error}</p>}
            {record && (
                <div style={styles.card}>
                    <h3>{record.name}</h3>
                    <p><strong>Name:</strong> {record.name}</p>
                    <p><strong>Email:</strong> {record.email}</p>
                    <p><strong>Note:</strong> {record.note}</p>
                    <p><strong>Id:</strong> {record.id}</p>
                </div>
            )}
        </div>
    );
}

const styles = {
    container: {
        textAlign: "center",
        marginTop: "50px",
        fontFamily: "Arial, sans-serif",
    },
    card: {
        backgroundColor: "#f8f9fa",
        padding: "20px",
        borderRadius: "10px",
        boxShadow: "0px 4px 6px rgba(0, 0, 0, 0.1)",
        maxWidth: "400px",
        margin: "auto",
        textAlign: "left",
    },
    error: {
        color: "red",
    },
};

export default CustomerDisplay;
