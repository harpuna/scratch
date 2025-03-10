import { useState, useEffect } from "react";

function CustomerTable() {
  const [customers, setCustomers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedCustomer, setSelectedCustomer] = useState(null);

  // row clicked
  const handleRowClick = (customer) => {
    setSelectedCustomer(customer);
  };

  // Handle input changes in the form
  const handleChange = (e) => {
    setSelectedCustomer({ ...selectedCustomer, [e.target.name]: e.target.value });
  };

  // Handle form submission to update customer data
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {

      const response = await fetch(`http://127.0.0.1:5000/api/customers/${selectedCustomer.id}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: selectedCustomer.name,
          email: selectedCustomer.email,
          note: selectedCustomer.note,
        }),
      });

      if (!response.ok) {
        alert(selectedCustomer.email)
        throw new Error("Failed to update customer.");
      }

      const updatedCustomer = await response.json();

      setCustomers(customers.map((customer) => (customer.id === updatedCustomer.id ? updatedCustomer : customer)));
      setSelectedCustomer(null); // Close the form after updating
    } catch (error) {
      alert(error.message)
    }
  };

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/customers") // Replace with your API URL
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch customer data");
        }
        return response.json();
      })
      .then((data) => {
        setCustomers(data);
        setLoading(false);
      })
      .catch((error) => {
        setError(error.message);
        setLoading(false);
      });
  }, []);

return (
    <div>
      {/* Table */}
      <table border="1">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Note</th>
          </tr>
        </thead>
        <tbody>
          {customers.map((customer) => (
            <tr key={customer.id} onClick={() => handleRowClick(customer)} style={{ cursor: "pointer" }}>
              <td>{customer.id}</td>
              <td>{customer.name}</td>
              <td>{customer.email}</td>
              <td>{customer.note}</td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* Form - Only show when a customer is selected */}
      {selectedCustomer && (
        // <div style={{ marginTop: "20px", border: "1px solid #ccc", padding: "10px", width: "300px" }}>
          <div className="form-container">
          <h3>Edit Customer</h3>
          <form onSubmit={handleSubmit}>
            <label>Name:</label>
            <input type="text" name="name" value={selectedCustomer.name} onChange={handleChange} required />
            <br />
            <label>Email:</label>
            <input type="email" name="email" value={selectedCustomer.email} onChange={handleChange} required />
            <br />
            <label>Note:</label>
            <input type="text" name="note" value={selectedCustomer.note} onChange={handleChange} />
            <br />
            <button type="submit" className="save-btn">Save</button>
            <button type="button" className="cancel-btn"onClick={() => setSelectedCustomer(null)}>Cancel</button>
          </form>
        </div>
      )}
    </div>
  );
};

export default CustomerTable;
