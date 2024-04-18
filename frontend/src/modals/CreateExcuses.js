import React, { useState } from 'react';
import Modal from 'react-modal';
import axios from 'axios';
import OpenModalBtn from './OpenModalBtn';


Modal.setAppElement('#root');

const CreateExcuses = ({ onExcuseCreated }) => {
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [message, setMessage] = useState('');
  const [selectedTag, setSelectedTag] = useState('');

   // List of tags to choose from
  const tags = [
    'Inexcusable',
    'Novelty Implementations',
    'Edge Cases',
    'Fucking',
    'Syntax Errors',
    'Predictable Problems',
    "Somebody Else's Problem",
    'Internet crashed',
    'Others',
    'Test-msg',
  ];

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (!selectedTag) {
        alert('Please, pick a tag');
        return; // Exit the function if no tag is selected
      }
      // Send data to db
      const response = await axios.post('http://localhost:5000/api/create', {
        tag: selectedTag,
        message: message,
      });

      // Clean fields
      setMessage('');

      // Close modal after submission with an alert + Clean tag
      alert(response.data.message);
      setModalIsOpen(false);
      setSelectedTag('');

      // Notify ExcuseGenerator that a new excuse has been created
      onExcuseCreated();
    } catch (error) {
      console.error('Error adding excuse:', error);
    }
  };

  return (
    <div className="creation-container">
      <OpenModalBtn onClick={() => setModalIsOpen(true)} />
      <Modal
        isOpen={modalIsOpen}
        onRequestClose={() => setModalIsOpen(false)}
        contentLabel="Create a new excuse"
        className="create-modal"
      >
        <button className="close-btn" onClick={() => setModalIsOpen(false)}>X</button>
        <h2 className="modal-h2">Add your own excuse</h2>

        <form className="create-form" onSubmit={handleSubmit}>
          <select
            id="tag"
            value={selectedTag}
            onChange={(e) => setSelectedTag(e.target.value)}
          >
            <option value="">Select a tag</option>
            {tags.map((tag) => (
              <option key={tag} value={tag}>
                {tag}
              </option>
            ))}
          </select>

          <input
            type="text"
            id="message"
            value={message}
            placeholder="Your excuse"
            onChange={(e) => setMessage(e.target.value)}
          />
          <button className="form-btn" type="submit">Create</button>
        </form>
      </Modal>
    </div>
  );
};

export default CreateExcuses;
