import { FC } from 'react';

interface PickerButtonProps {
  label: string;
  disabled?: boolean;
  onClick: () => void;
}

export const PickerButton: FC<PickerButtonProps> = ({ label, disabled, onClick }) => (
  <button className="button secondary" onClick={onClick} disabled={disabled}>
    {label}
  </button>
);








