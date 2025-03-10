import {useState} from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function Header() {
    const [count, setCount] = useState(0)

    return (
        <>
            <header className="header">
                <table width="100%">
                    <tr>
                        <td className="logo_sm">
                            Scratch Demo
                        </td>
                        <td>
                            <ul className="nav">
                                <li><a href="/">Home</a></li>
                                <li><a href="/">About</a></li>
                                <li><a href="/">Services</a></li>
                                <li><a href="/">Contact</a></li>
                                <li>
                                </li>
                            </ul>

                        </td>
                        <td width={40}>
                            <img src={reactLogo} className="logo_sm react" alt="React logo"/>
                        </td>
                    </tr>
                </table>
            </header>

            <h2>Welcome to React Scratch!</h2>
            <div>
                <h3>Meet our CUSTOMERS</h3>
            </div>
            <br/>

        </>
    )
}

export default Header
