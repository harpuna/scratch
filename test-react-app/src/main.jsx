import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import Customer from './Customer.jsx'
import Header from './Header.jsx'
import CustomerDisplay from './CustomerDisplay.jsx'
import CustomerTable from './CustomerTable.jsx'
import CustomerTable0 from './CustomerTable_0.jsx'
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Header />
    <CustomerTable />
  </StrictMode>,
)
