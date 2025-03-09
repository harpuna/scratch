import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import Customer from './Customer.jsx'
import CustomerDisplay from './CustomerDisplay.jsx'
import CustomerTable from './CustomerTable.jsx'
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
    <CustomerTable />
  </StrictMode>,
)
