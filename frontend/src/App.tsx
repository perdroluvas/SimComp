import "./index.css";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Physical from "./home/physical";
import Network from "./home/network";
import Simulation from "./home/simulation";
import Result from "./home/result";

export function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Navigate to="/physical" replace />} />
        <Route path="/physical" element={<Physical />} />
        <Route path="/network" element={<Network />} />
        <Route path="/simulation" element={<Simulation />} />
        <Route path="/result" element={<Result />} />
      </Routes>
    </Router>
  );
}

export default App;
