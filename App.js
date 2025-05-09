import React, { useState } from 'react';
import { Button, Card, CardContent } from '@/components/ui/button';

const App = () => {
    const [recommendations, setRecommendations] = useState([]);
    const [error, setError] = useState('');

    const fetchRecommendations = async () => {
        try {
            const response = await fetch('http://localhost:5000/api/recommendations');
            if (!response.ok) throw new Error('Network response was not ok');
            const data = await response.json();
            setRecommendations(data);
        } catch (err) {
            setError('Error fetching data');
            console.error(err);
        }
    };

    return (
        <div className="container mx-auto p-4">
            <h2 className="text-2xl font-bold mb-4">Personalized E-Learning Recommendations</h2>
            <Button onClick={fetchRecommendations} className="mb-4">Fetch Recommendations</Button>
            {error && <p className="text-red-500">{error}</p>}
            {recommendations.map((item, index) => (
                <Card key={index} className="mb-2 p-2">
                    <CardContent>
                        <p>Student ID: {item.student_id}</p>
                        <p>Recommendation: {item.recommendation}</p>
                    </CardContent>
                </Card>
            ))}
        </div>
    );
};

export default App;


The App.js file for the frontend logic is ready in the canvas. Let me know if you need any modifications or additional functionality.
